import React, { useRef, useEffect } from 'react';
import './Textbox.css'; // Importa el archivo de estilos CSS

function MyInterface() {
  const textareaRef = useRef(null); // Referencia al elemento textarea

  useEffect(() => {
    // Función para actualizar los números de línea cuando cambia el contenido del textarea
    const updateLineNumbers = () => {
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
    };

    // Llamar a la función de actualización de números de línea cuando se monta el componente
    updateLineNumbers();

    // Adjuntar un evento de cambio al textarea para actualizar los números de línea cuando cambia el contenido
    const textareaCurrent = textareaRef.current; // Copia el valor de textareaRef.current
    textareaCurrent.addEventListener('input', updateLineNumbers);

    // Limpiar el evento de cambio cuando se desmonta el componente para evitar pérdidas de memoria
    return () => {
      textareaCurrent.removeEventListener('input', updateLineNumbers);
    };
  }, []); // Solo se ejecutará una vez cuando se monte el componente

  return (
    <div style={{ display: 'grid', gridTemplateRows: 'auto 1fr auto', gridTemplateColumns: '1fr' }}>
      <div style={{ backgroundColor: 'pink', height: '50px' }}>
        <Menu />
      </div>
      <div style={{ backgroundColor: 'orange' }}>
        <Textbox textareaRef={textareaRef} />
      </div>
      <div style={{ backgroundColor: 'purple' }}>
        <Table />
      </div>
      <div style={{ backgroundColor: 'blue' }}>
        <Interface />
      </div>
    </div>
  );
}

//Menu
function Menu() {
  return <div>This is the menu</div>;
}

//Tabla de simbolos
function Table() {
  return (
    <table>
      <tr>
        <td>Row 1, Cell 1</td>
        <td>Row 1, Cell 2</td>
      </tr>
      <tr>
        <td>Row 2, Cell 1</td>
        <td>Row 2, Cell 2</td>
      </tr>
    </table>
  );
}

//Consola
function Interface() {
  return <div>This is the interface</div>;
}

//Cuadro de texto
function Textbox({ textareaRef }) {
  return (
    <div className="textbox-container">
      {/* Contenedor para los números de línea */}
      <div className="line-numbers"></div>
      {/* Textarea */}
      <textarea
        ref={textareaRef}
        className="textbox"
        style={{
          width: '500px', // Ancho fijo
          height: '300px', // Altura fija
          resize: 'none', // Evita que el usuario pueda redimensionar el cuadro de texto
          overflowX: 'auto', // Muestra una barra de desplazamiento horizontal cuando sea necesario
          overflowY: 'auto', // Muestra una barra de desplazamiento vertical cuando sea necesario
          fontSize: '20px', // Tamaño de la fuente
          lineHeight: '20px', // Ajusta este valor según el interlineado deseado entre los números de línea
        }}
      ></textarea>
    </div>
  );
}

export default MyInterface;
