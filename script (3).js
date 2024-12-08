// Inicializar EmailJS
emailjs.init('YOUR_PUBLIC_KEY'); // Substitua 'YOUR_PUBLIC_KEY' pela sua chave pública fornecida pelo EmailJS

// Referência ao formulário
const form = document.getElementById('contact-form');

// Evento de envio do formulário
form.addEventListener('submit', function (event) {
    event.preventDefault(); // Evita o recarregamento da página

    // Coletar os dados do formulário
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const mensagem = document.getElementById('mensagem').value;

    // Parâmetros para o template do EmailJS
    const templateParams = {
        from_name: nome,
        from_email: email,
        message: mensagem,
    };

    // Enviar o e-mail usando EmailJS
    emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', templateParams)
        .then(function (response) {
            alert('Mensagem enviada com sucesso!');
            form.reset(); // Limpar o formulário após o envio
        }, function (error) {
            alert('Erro ao enviar mensagem, tente novamente.');
            console.error('Erro:', error);
        });
});
