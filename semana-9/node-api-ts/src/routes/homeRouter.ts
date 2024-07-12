import express from "express"; // -> acceso a get post put delete reemplazando la app
import { index } from "../controller/homeController";

const router = express.Router();

router.get("/", index);

export default router;