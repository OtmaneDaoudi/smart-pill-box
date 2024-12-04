const addBtn = document.getElementsByClassName("addBtn")[0]
const form = document.getElementById("targetForm")

addBtn.addEventListener("click", () => {
    form.classList.toggle("hidden")
})

function renderTable(data)
{
    const actionsCol = {
        name: 'Actions',
        formatter: (_, row) => gridjs.html(`<a class="delete action" href='/medication/medication/delete/${row.cells[0].data}'>Delete</a>`)
    }
    
    new gridjs.Grid({
        columns: ["ID", "Name", "Instructions", actionsCol],
        data,
        sort: {
        multiColumn: false
    },
        height: "10"
       }).render(document.getElementById("wrapper"));
}

