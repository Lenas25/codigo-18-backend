import type { Request, Response } from 'express'

export const index = (_req: Request, res: Response) => {
  return res.json({ message: "Hello World" });
}
