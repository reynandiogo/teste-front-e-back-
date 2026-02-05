const form = document.getElementById('meuForm');

form.addEventListener('submit', async function (event) {
  event.preventDefault();

  const formData = new FormData(form);
  const dados = Object.fromEntries(formData);

  try {
    const resposta = await fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dados)
    });

    const resultado = await resposta.json();

    const divResposta = document.getElementById('resposta');
    if (resultado.sucesso) {
      divResposta.textContent = 'Login bem-sucedido!';
    } else {
      divResposta.textContent = 'Usuário ou senha inválidos.';
    }

  } catch (erro) {
    console.error('Erro na requisição:', erro);
  }
});
