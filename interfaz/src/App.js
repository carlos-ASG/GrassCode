import React, { useRef, useState, useEffect } from 'react';
import './CuadroTexto.css'; // Importa el archivo de estilos CSS
import { saveAs } from 'file-saver'; // Importa la función de FileSaver.js

function MyInterface() {
  const textareaRef = useRef(null); // Referencia al elemento textarea
  const [textareaContent] = useState(''); // Estado para almacenar el contenido del textarea
  const [fileInputKey, setFileInputKey] = useState(0); // Estado para reiniciar el input de archivo
  const [tableData, setTableData] = useState([
    // Ejemplo de datos iniciales
    { id: 1, Nombre: '', Lexema: '' }
  ]);

  useEffect(() => {
    // Función para actualizar los números de línea y sincronizar el scroll vertical
    const updateLineNumbersAndSyncScroll = () => {
      const textarea = textareaRef.current;
      const lineNumbersContainer = document.querySelector('.line-numbers');
      lineNumbersContainer.innerHTML = ''; // Limpiar los números de línea actuales

      // Contar el número de líneas en el texto
      const linesCount = textarea.value.split('\n').length;

      // Generar los números de línea y agregarlos al contenedor
      for (let i = 1; i <= linesCount; i++) {
        const lineNum = document.createElement('div');
        lineNum.textContent = i;
        lineNumbersContainer.appendChild(lineNum);
      }

      // Sincronizar el scroll vertical
      lineNumbersContainer.scrollTop = textarea.scrollTop;
    };

    // Llamar a la función de actualización y sincronización cuando se monta el componente
    updateLineNumbersAndSyncScroll();

    // Adjuntar un evento de cambio al textarea para actualizar y sincronizar los números de línea
    const textareaCurrent = textareaRef.current; // Copia el valor de textareaRef.current
    textareaCurrent.addEventListener('input', updateLineNumbersAndSyncScroll);
    textareaCurrent.addEventListener('scroll', updateLineNumbersAndSyncScroll);

    // Limpiar los eventos cuando se desmonta el componente para evitar pérdidas de memoria
    return () => {
      textareaCurrent.removeEventListener('input', updateLineNumbersAndSyncScroll);
      textareaCurrent.removeEventListener('scroll', updateLineNumbersAndSyncScroll);
    };
  }, []); // Solo se ejecutará una vez cuando se monte el componente

  // Función para guardar el contenido del textarea en un archivo
  const handleSave = () => {
    const content = textareaRef.current.value;
    const blob = new Blob([content], { type: 'text/plain' });
    saveAs(blob, 'textarea_content.txt');
  };

  // Función para manejar la apertura de archivos
  const handleOpen = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
  
    reader.onload = (e) => {
      const content = e.target.result;
      textareaRef.current.value = content; // Establecer el contenido directamente en el textarea
      
      // Contar el número de líneas en el archivo
      const linesCount = content.split('\n').length;
  
      // Generar los números de línea y agregarlos al contenedor
      const lineNumbersContainer = document.querySelector('.line-numbers');
      lineNumbersContainer.innerHTML = ''; // Limpiar los números de línea actuales
      for (let i = 1; i <= linesCount; i++) {
        const lineNum = document.createElement('div');
        lineNum.textContent = i;
        lineNumbersContainer.appendChild(lineNum);
      }
    };
  
    reader.readAsText(file);
    setFileInputKey(prevKey => prevKey + 1); // Reiniciar el input de archivo para permitir la selección del mismo archivo
  };

  // Función para ejecutar el código
  const handleExecute = (codigo_fuente) => {
    const url = 'http://localhost:5000/lexico';
    const data = { codigo_fuente }; // Crear el objeto de datos con el valor obtenido del cuadro de texto
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({"codigo_fuente":data})
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('Respuesta recibida:', data);
      // Aquí puedes manejar los datos de la respuesta, si es necesario
    })
    .catch(error => {
      console.error('Hubo un problema con la solicitud:', error);
    });
  };

  const handleChange = (id, column, value) => {
    // Actualizar el valor de una celda específica
    const newData = tableData.map(row =>
      row.id === id ? { ...row, [column]: value } : row
    );
    setTableData(newData);
  };

  const handleAddRow = () => {
    // Agregar una nueva fila con celdas vacías
    const newRow = { id: Date.now(), column1: '', column2: '' };
    setTableData([...tableData, newRow]);
  };

  return (
    <div style={{ 
      display: 'grid', // Establece el contenedor como un grid
      gridTemplateRows: 'auto 1fr auto', // Define las filas del grid
      gridTemplateColumns: '1fr' // Define una única columna
    }}>    
      <div>
        <Menu handleSave={handleSave} textareaRef={textareaRef} handleExecute={handleExecute} /> {/* Pasa textareaRef y handleExecute como propiedades */}
      </div>
      <div>
        <Textbox textareaRef={textareaRef} content={textareaContent} />
      </div>
      <div>
        <Console />
      </div>
      <div className="table-container">     
        <Table tableData={tableData} handleChange={handleChange} />
        <button onClick={handleAddRow}>Agregar Fila</button>
      </div>
      <input
        type="file"
        key={fileInputKey} // Clave única para reiniciar el input de archivo
        onChange={handleOpen}
        style={{ display: 'none' }}
        id="file-input"
      />
    </div>
  );
}

// Menu
function Menu({ textareaRef, handleExecute }) { // Recibe textareaRef y handleExecute como propiedades
  const handleExecuteClick = () => {
    const codigo_fuente = textareaRef.current.value; // Obtener el valor actual del cuadro de texto
    handleExecute(codigo_fuente); // Llamar a handleExecute con el contenido del cuadro de texto
  };

  const handleSaveAs = () => {
    const content = textareaRef.current.value;
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);

    // Crear un elemento <a> temporal
    const a = document.createElement('a');
    a.href = url;
    a.download = 'Archivo.txt'; // Nombre del archivo por defecto

    // Agregar el elemento <a> al DOM y hacer clic en él para abrir el cuadro de diálogo "Guardar como"
    document.body.appendChild(a);
    a.click();

    // Eliminar el elemento <a> del DOM
    document.body.removeChild(a);

    // Liberar el objeto URL creado
    URL.revokeObjectURL(url);
  };

  return (
    <div className="menu-container" style={{ 
      backgroundColor: '#94ddbc',
      width: '80%',
      paddingLeft: '50px',
      paddingRight: '100px',
      marginTop: '10px',
      marginBottom: '5px',
      marginLeft: '50px'
    }}>
      <button 
        onClick={handleSaveAs}
        style={{ 
          backgroundColor: '#88bb92',
          color: 'white',
          padding: '8px',
          marginRight: '10px',
          marginTop: '10px',
          marginBottom: '10px',
          border: 'none',
          fontSize: '15px',
          fontFamily: 'Arial'
        }}
      >Guardar</button>
      <button 
        onClick={handleExecuteClick}
        style={{ 
          backgroundColor: '#88bb92',
          color: 'white',
          padding: '8px',
          marginRight: '10px',
          marginTop: '10px',
          marginBottom: '10px',
          border: 'none',
          fontSize: '15px',
          fontFamily: 'Arial'
        }}
      >Ejecutar</button>
      <label 
        htmlFor="file-input"
        style={{ 
          backgroundColor: '#88bb92',
          color: 'white',
          padding: '8px',
          marginTop: '10px',
          marginBottom: '10px',
          fontSize: '16px',
          fontFamily: 'Arial'
        }}
      >Abrir</label>
    </div>
  );
}

// Consola
function Console() {
  return (
    <div className="textbox-container">
      {/* Textarea */}
      <textarea
        className="textbox"
        style={{
          width: '100%',
          height: '100px',
          resize: 'none',
          overflow: 'auto',
          fontSize: '20px',
          lineHeight: '20px',
          whiteSpace: 'nowrap',
          border: '1px solid black',
        }}
      ></textarea>
    </div>
  );
}

// Cuadro de texto
function Textbox({ textareaRef, content }) {
  return (
    <div className="textbox-container">
      {/* Contenedor para los números de línea */}
      <div className="line-numbers"></div>
      {/* Textarea */}
      <textarea
        ref={textareaRef}
        className="textbox"
        style={{
          width: '100%',
          height: '300px',
          resize: 'none',
          overflow: 'auto',
          fontSize: '20px',
          lineHeight: '20px',
          whiteSpace: 'nowrap',
          border: '1px solid black',
          fontFamily: 'Arial'
        }}
        defaultValue={content}
      ></textarea>
    </div>
  );
}

// Tabla
function Table({ tableData, handleChange }) {
  // Determina si se debe aplicar el scroll vertical
  const shouldApplyScroll = tableData.length >= 13;

  return (
    <div style={{ overflowY: shouldApplyScroll ? 'scroll' : 'auto', maxHeight: shouldApplyScroll ? '450px' : 'auto' }}>
      <div style={{ width: '100%', overflowX: 'auto' }}>
        <table style={{ borderCollapse: 'collapse', width: '92%', fontSize: '14px' }}>
          <thead>
            {/* Renderizar la primera fila de encabezados fija */}
            <tr>
              {Object.keys(tableData[0] || {}).map(key => (
                key !== 'id' && (
                  <th key={key} style={{ border: '1px solid black', background: 'White', padding: '4px', textAlign: 'center', minHeight: '24px', position: 'sticky', top: 0, zIndex: 1 }}>
                    {key}
                  </th>
                )
              ))}
            </tr>
          </thead>
          <tbody>
            {/* Renderizar filas de datos */}
            {tableData.map(row => (
              <tr key={row.id}>
                {/* Renderizar celdas de datos */}
                {Object.entries(row).map(([column, value]) => (
                  column !== 'id' && (
                    <td key={column} style={{ border: '1px solid black', background: 'White', padding: '4px', textAlign: 'center', minHeight: '24px' }}>
                      <input
                        type="text"
                        value={value}
                        onChange={e => handleChange(row.id, column, e.target.value)}
                        style={{ border: 'none', outline: 'none', width: '100%', textAlign: 'center' }}
                      />
                    </td>
                  )
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default MyInterface;
