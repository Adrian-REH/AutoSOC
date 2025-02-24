
const stripe = Stripe('pk_test_51Qn0ZQGfkydL0eslH568mPRTnGR2wLBsyTCvRSHjD5ZrIFGbgFSZtZqi9sUP2nbMGC2wsPn06HTp6wzD3YCIABoP00kGrejnzX'); // Sustituye con tu clave pública de Stripe
const elements = stripe.elements();
const donationInput = document.getElementById('donation-input');
const donationAmountDisplay = document.getElementById('donation-amount');

const card = elements.create('card');
card.mount('#card-element');

/**
 * Escucho si esta utilizando WebDriver y ejecuto una peticion hacia mi BackEnd para tomar accion.
 */
document.addEventListener('DOMContentLoaded', async function () {
  if (navigator.webdriver || (window.chrome && window.chrome.webstore) || navigator.plugins.length === 0 || navigator.userAgent.includes("HeadlessChrome")) {
    console.log("WebDriver detectado.");
    document.body.innerHTML = `
    <div style="
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      background-color: black;
      color: white;
      font-family: Arial, sans-serif;
      text-align: center;
    ">
      <h1>🚫 Acceso Denegado 🚫</h1>
      <p>Se ha detectado el uso de WebDriver o un entorno automatizado.</p>
      <p>Si crees que esto es un error, por favor contáctanos.</p>
    </div>
  `;

    // Evita cualquier interacción posterior
    document.body.style.pointerEvents = "none";
    try {
      const ipResponse = await fetch('https://api64.ipify.org?format=json');
      const ipData = await ipResponse.json();
      const userIp = ipData.ip;

      const userData = {
        ip: userIp,
        userAgent: navigator.userAgent,
        language: navigator.language,
        platform: navigator.platform,
        screen: {
          width: screen.width,
          height: screen.height
        },
        timestamp: new Date().toISOString()
      };
      await fetch('http://localhost:9090/api/actions/notify-webdriver-detection/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });
    } catch (err) {
      console.log("Error al enviar los datos")
    }


  }
});

const form = document.getElementById('payment-form');
const listPayments = document.getElementById('payments-list');

function addAceptedPayment() {
  const li = document.createElement('li');
  li.classList.add('card');
  li.textContent = `Donacion de $${(parseInt(donationInput.value) || 0)} Aceptada`;

  li.classList.add('green');

  listPayments.appendChild(li);
}

function addCancelPayment() {
  const li = document.createElement('li');
  li.classList.add('card');

  li.textContent = `Donacion de $${(parseInt(donationInput.value) || 0)} Cancelada`;

  li.classList.add('red');

  listPayments.appendChild(li);
}

function updateDonationAmount() {
  const amount = parseFloat(donationInput.value) || 0;  // Evitar NaN
  donationAmountDisplay.textContent = amount.toFixed(2);  // Mostrar el monto con dos decimales
}

donationInput.addEventListener('input', updateDonationAmount);

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  // Crear el token para el pago
  const { token, error } = await stripe.createToken(card);
  if (error) {
    console.error(error);
    alert('Hubo un error con el pago: ' + error.message);
  } else {
    console.log('Token:', token);

    const response = await fetch('https://service.local.com/api/payments/process-payment/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        token: token.id,
        amount: parseInt(donationInput.value) || 0,
        email: document.getElementById('email').value
      })
    });

    if (response.ok) {
      addAceptedPayment()
    } else {
      addCancelPayment()
    }
  }
});

