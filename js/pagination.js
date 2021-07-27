function pagination(){
	var table = new Tabulator("#example-table", {
    pagination:"local", //enable local pagination.
    paginationSize:5, // this option can take any positive integer value
	});
}