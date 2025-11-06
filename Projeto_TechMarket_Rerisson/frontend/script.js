function validarFormulario() {
  const cpf = document.getElementById('cpf').value;
  const nascimento = document.getElementById('nascimento').value;
  const telefone = document.getElementById('telefone').value;

  if (cpf.length !== 11) {
    alert('CPF deve conter 11 dígitos');
    return;
  }
  const dataNasc = new Date(nascimento);
  if (isNaN(dataNasc)) {
    alert('Data de nascimento inválida');
    return;
  }
  if (telefone.length < 10 || telefone.length > 11) {
    alert('Telefone inválido');
    return;
  }
  alert('Formulário válido!');
}
