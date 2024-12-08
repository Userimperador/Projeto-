// Exemplo básico para manipulação do formulário
const form = document.getElementById('contact-form');

form.addEventListener('submit', function (event) {
    event.preventDefault(); // Previne o envio padrão do formulário

    // Obtenha os valores do formulário
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const mensagem = document.getElementById('mensagem').value;

    // Exibir os dados no console (apenas para demonstração)
    console.log('Nome:', nome);
    console.log('Email:', email);
    console.log('Mensagem:', mensagem);

    // Mensagem de sucesso (simulada)
    alert('Mensagem enviada com sucesso! Obrigado por entrar em contato.');

    // Limpar o formulário
    form.reset();
});
