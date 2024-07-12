import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient(); // instancia para el uso en controladores

export default prisma;