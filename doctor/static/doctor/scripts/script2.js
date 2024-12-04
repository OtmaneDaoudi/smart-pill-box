function renderTable(data)
{
    console.log(data)

    // const actionsCol = {
    //     name: 'Actions',
    //     formatter: (_, row) => gridjs.html(`
    //         <span>
    //             <a class="delete action" href='/${row.cells[0].data}'>Delete</a>
    //             <a href="/medication/prescription/${row.cells[0].data}" class="action green ">Prescription</a>
    //             <a href="" class="action blue">Logs</a>
    //         </span>`)
    // }
    
    new gridjs.Grid({
        columns: ["ID", "Medication", "Period (Prescription)", "Period (Taken)", "Date"],
        data,
        sort: {
            multiColumn: false
        },
        search: true,
        height: "10"
       }).render(document.getElementById("wrapper"));
}