import 'dotenv/config'; // -> importar dotenv
// importar express
import express from "express"; // -> forma antigua de importar
import homeRouter from "./routes/homeRouter";
import bookRouter from "./routes/bookRouter";
// const { v4: uuidv4 } = require('uuid');

// instanciar express en una variable
const app = express();

// para que express sea capaz de entender json y poder recibirlo
app.use(express.json());
app.use('/api/v1', homeRouter);
app.use('/api/v1', bookRouter);

// response -> es lo que usamos para poder responderle al cliente
// request -> donde esta la infoque envia el cliente

// el servidor escucha en el puerto 6000

app.listen(9000, () => {
  console.log("El servidor inicio en http://localhost:9000");
});
