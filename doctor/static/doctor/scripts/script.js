function renderTable(data)
{
    console.log(data)

    const actionsCol = {
        name: 'Actions',
        formatter: (_, row) => gridjs.html(`
            <span>
                <a class="delete action" href='/${row.cells[0].data}'>Delete</a>
                <a href="/medication/prescription/${row.cells[0].data}" class="action green ">Prescription</a>
                <a href="/doctor/alerts/${row.cells[0].data}" class="action blue">Alerts</a>
            </span>`)
    }
    
    new gridjs.Grid({
        columns: ["ID", "First Name", "Last name", "Email", actionsCol],
        data,
        sort: {
            multiColumn: false
        },
        search: true,
        height: "10"
       }).render(document.getElementById("wrapper"));
}

