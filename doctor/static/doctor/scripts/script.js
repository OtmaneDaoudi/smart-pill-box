function renderTable(data)
{
    console.log(data)

    const actionsCol = {
        name: 'Actions',
        formatter: (_, row) => gridjs.html(`<a class="delete" href='/${row.cells[0].data}'>Delete</a>`)
    }
    
    new gridjs.Grid({
        columns: ["ID", "First Name", "Last name", "Email", actionsCol],
        data,
        sort: {
        multiColumn: false
    },
        height: "10"
       }).render(document.getElementById("wrapper"));
}

