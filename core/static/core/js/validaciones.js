function validarFormulario() {
    let x = document.forms["myForm"]["fname"].value;
    if (x == "") {
      alert("El campo debe ser rellenado");
      return false;
    }
  }