const index = (req, res)=>{
  return res.json({ message: "Hola Mundo" });
}

module.exports = { index }