import { initMercadoPago, Wallet, CardPayment } from "@mercadopago/sdk-react";

// Aquí se inicializa el SDK de Mercado Pago con el public key de tu aplicación
initMercadoPago("TEST-e74475e4-2791-423a-a452-318c33af27f5");

import "./App.css";

function App() {
  return (
    <>
      <main>
        <section>
          <h1>Integrando Mercado Pago</h1>
          {/* es necesario crear un endpoint para autenticar en el backend, cuando se obtenga el preference id aqui se coloca como inicializar un atributo de preference id para hacer el pago y luego te devuelve a la ruta pero con un query param segun indicado en el backend */}
          {/* <Wallet initialization={{
          preferenceId: "1098491586-c1350892-2642-45c8-8528-4a1e136009cc",
        }} /> */}
          <CardPayment
            initialization={{ amount: 1000 }}
            customization={{
              visual: {
                style: {
                  theme: "flat",
                },
              },
              paymentMethods: {
                creditCard: "all",
                debitCard: "all",
                ticket: "all",
                bankTransfer: "all",
                onboarding_credits: "all",
                maxInstallments: 12,
              },
            }}
            onSubmit={async (param) => {
              const response = await fetch(
                "http://127.0.0.1:8000/api/v1/create-payment/",
                {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json",
                  },
                  body: JSON.stringify({
                    transaction_amount: param.transaction_amount,
                    token: param.token,
                    description: "Venta de S/500",
                    installments: param.installments,
                    payment_method_id: param.payment_method_id,
                    email: param.payer.email,
                    type: param.payer.identification.type,
                    number: param.payer.identification.number,
                  }),
                }
              );
              const data = await response.json();
              console.log(data);
            }}
          />
        </section>
      </main>
    </>
  );
}

export default App;
