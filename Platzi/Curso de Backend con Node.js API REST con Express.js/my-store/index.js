const express = require('express');
const cors = require('cors');
const routerApi = require('./routes')
const { logErrors,errorHandler,boomErrorHandler } = require('./middlewares/error.handler')

const port = process.env.PORT || 3000;
const app = express();

app.use(express.json())

const whiteList = []//['http://localhost:3000/']
const options = {
  origin: (origin, callback) => {
    if(whiteList.includes(origin) || !origin){
      callback(null,true)
    }else{
      callback(new Error('no permitido'))
    }
  }
}
app.use(cors(options))

app.get('/', (req, res) => {
  res.send('Hola mi server en express');
});

app.get('/nueva-ruta', (req, res) => {
  res.send('Hola, soy una nueva ruta');
});

app.listen(port, () => {
  console.log('Example app listening at ' + port);
});

routerApi(app)
app.use(logErrors)
app.use(boomErrorHandler)
app.use(errorHandler)
