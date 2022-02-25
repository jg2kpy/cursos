const express = require('express')
const session = require('express-session')
const { engine } = require ('express-handlebars');
const bp = require('body-parser')
const fs = require('fs')

const app = express()
const PORT = 3000



//Middlewares

app.use(bp.json())
app.use(bp.urlencoded({ extended: true }))
app.use(session({
    secret: 'test',
    resave: false,
    saveUninitialized: false,
}))

app.use(express.urlencoded({ extended: true }))

app.engine('handlebars', engine());
app.set('view engine', 'handlebars');
app.set("views", "./views");

// Login

function login(req, res, next){
    if(!req.session.userId){
        res.redirect('login')
    }else{
        next()
    }
}

// Db

const users = JSON.parse(fs.readFileSync('db.json'))

//Routes

app.get('/home', login, (req, res) => {
    res.send('Home page, must be logged in to access')
})

app.get('/login', (req, res) => {
    res.render('login')
})

app.post('/login', (req, res) => {
    if (!req.body.email || !req.body.password){
        return res.status(400).send('Fiil all de fields')
    }
    const user = users.find(user => user.email === req.body.email)
    if(!user || user.password !== req.body.password){
        return res.status(400).send('Invalid credentials')
    }
    req.session.userId = user.id
    console.log(req.session)
    res.redirect('/home')
})

//Server

app.listen(PORT, () => console.log('Listening on port', PORT))