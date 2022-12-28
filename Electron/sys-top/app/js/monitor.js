const path = require('path')
const { ipcRenderer } = require('electron')
const osu = require('node-os-utils')
const cpu = osu.cpu
const mem = osu.mem
const os = osu.os

let cpuOverLoad
let alertFrequency

//  Get settings & values
ipcRenderer.on('settings:get', (e, settings) => {
    cpuOverLoad = +settings.cpuOverLoad
    alertFrequency = +settings.alertFrequency
})


//  Run every 2 seconds
setInterval(() => {
    //  CPU USAGE
    cpu.usage().then(info => {
        document.getElementById('cpu-usage').innerText = `${info.toFixed(2)}%`
        document.getElementById('cpu-free').innerText = `${(100 - info).toFixed(2)}%`
        document.getElementById('cpu-progress').style.width = `${info}%`
        //  Make progress bar if overload
        if(info > cpuOverLoad){
            document.getElementById('cpu-progress').style.background = 'red'
        }else{
            document.getElementById('cpu-progress').style.background = 'var(--primary-color)'
        }

        //  Check overload
        if(info > cpuOverLoad && runNotify(alertFrequency)){
            notifyUser({
                title: 'CPU Overload',
                body: `CPU is over ${cpuOverLoad}`,
                icon: path.join(__dirname, 'img', 'icon.png')
            })
            localStorage.setItem('lastNotify', +new Date())
        }
    })

    //  Uptime
    document.getElementById('sys-uptime').innerText = secondsToDhms(os.uptime())

}, 2000)



//  Set model
document.getElementById('cpu-model').innerText = cpu.model()

//  Computer name
document.getElementById('comp-name').innerText = os.hostname()

//  OS
document.getElementById('os').innerText = `${os.type()} ${os.arch()}`

//  Total Men
mem.info().then(info => {
    document.getElementById('mem-total').innerText = info.totalMemMb
})

//  Show days, hours, mins, sec
function secondsToDhms(seconds){
    seconds = +seconds
    const d = Math.floor(seconds / (3600 * 24))
    const h = Math.floor((seconds) % (3600 * 24) / 3600)
    const m = Math.floor((seconds % 3600)  / 60)
    const s = Math.floor(seconds % 60)
    return `${d}d, ${h}h, ${m}m, ${s}s`
}

//  Send a notification 
function notifyUser(options){
    new Notification(options.title, options)
}

//  Check how much time pass since notification
function runNotify(frequency){
    if(localStorage.getItem('lastNotify') === null){
        localStorage.setItem('lastNotify', +new Date())
        return true
    }
    const notifyTime = new Date(parseInt(localStorage.getItem('lastNotify')))
    const now = new Date()
    const difftime = Math.abs(now - notifyTime)
    const minutesPassed = Math.ceil(difftime / (1000 * 60))
    
    if(minutesPassed > frequency){
        return true
    }else{
        return false
    }
}
