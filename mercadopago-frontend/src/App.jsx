
import { initMercadoPago, Wallet } from '@mercadopago/sdk-react'

// Aquí se inicializa el SDK de Mercado Pago con el public key de tu aplicación
initMercadoPago("TEST-e74475e4-2791-423a-a452-318c33af27f5")

import './App.css'

function App() {

  return (
    <>
      <main>
      <section>
        <h1>Integrando Mercado Pago</h1>
        {/* es necesario crear un endpoint para autenticar en el backend, cuando se obtenga el preference id aqui se coloca como inicializar un atributo de preference id para hacer el pago y luego te devuelve a la ruta pero con un query param segun indicado en el backend */}
        <Wallet initialization={{
          preferenceId: "1098491586-c1350892-2642-45c8-8528-4a1e136009cc",
        }} />
      </section>
      </main>

    </>
  )
}

export default App
