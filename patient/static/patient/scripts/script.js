const morning_todos = document.querySelectorAll("#morning .upnext .task")
const aftenoon_todos = document.querySelectorAll("#afternoon .upnext .task")
const evening_todos = document.querySelectorAll("#evening .upnext .task")

const overlay = document.getElementsByClassName("overlay")[0]
const modal = document.getElementsByClassName("modal")[0]
const dismissBtn = document.getElementById("dismiss-modal")
const reminderBtn = document.getElementById("reminderBtn")
const reminderSelect = document.getElementById("timer")
let notification_medications = document.getElementById("notification-medications")
let notification_eventListener = null

let NOTIFICATION_INTERVAL = 2000

function show_modal()
{
    overlay.classList.remove("hidden")
    modal.classList.remove("hidden")
}

function hide_modal()
{
    overlay.classList.add("hidden")
    modal.classList.add("hidden")
}

dismissBtn.addEventListener("click", () => hide_modal())
overlay.addEventListener("click", () => hide_modal())
reminderBtn.addEventListener("click", () => {
    // get sleected option
    NOTIFICATION_INTERVAL = Number(reminderSelect.value) * 1000
    clearInterval(notification_eventListener)
    notification_eventListener = setInterval(() => {
        load_notifications()
    }, NOTIFICATION_INTERVAL);

    hide_modal()
})

function display_notification(medications)
{
    while(notification_medications.firstChild){
        notification_medications.removeChild(notification_medications.firstChild);
    }
    for(const medication of medications)
    {
        const newLi = document.createElement("li")
        newLi.textContent = medication

        notification_medications.appendChild(newLi)
    }

    show_modal()
}


function load_notifications()
{
    const period_to_tasks = {
        "M": morning_todos,
        "A": aftenoon_todos,
        "E": evening_todos
    }
    
    // what period is it
    const now = new Date();
    let period = null;
    if (now.getHours() >= 6 && now.getHours() <= 12) period = "M";
    else if (now.getHours() > 12 && now.getHours() <= 18) period = "A";
    else period = "E";


    let medications = []
    if (period_to_tasks[period].length > 0)
    {
        for(let task of period_to_tasks[period])
            medications.push(task.querySelector('p').textContent)
    }
    
    if(medications.length > 0) // schedule notifications
    {
        console.log("boom")
        display_notification(medications)
    }
}

notification_eventListener =  setInterval(() => {
    load_notifications()
}, NOTIFICATION_INTERVAL);