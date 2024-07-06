const { PrismaClient } = require("@prisma/client");

const prisma = new PrismaClient(); // instancia para el uso en controladores

module.exports = prisma;