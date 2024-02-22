function displayAll() {
    const xhttp = new XMLHttpRequest();
    const url = "https://amhep.pythonanywhere.com/grades";
    xhttp.open("GET", url, true);
    xhttp.send();
    xhttp.onload = function () {
        document.getElementById("0").innerHTML = this.responseText;
    };
}

function displayStudent() {
    var student = document.getElementById("displayStu").value;
    const xhttp = new XMLHttpRequest();
    const url = "https://amhep.pythonanywhere.com/grades/";
    xhttp.open("GET", url + student, true);
    xhttp.send();
    xhttp.onload = function () {
        document.getElementById("1").innerHTML = this.responseText;
    };
}



function addStudent() {
    var addStudent = document.getElementById("addStu").value;
    var addGrade = document.getElementById("addGrade").value;
    const xhttp = new XMLHttpRequest();
    const url = "https://amhep.pythonanywhere.com/grades";
    xhttp.open("POST", url);
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = { "name": addStudent, "grade": Number(addGrade) };
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function (){
        data = JSON.parse(this.responseText);
        Object.entries(data).forEach(([key, value]) => {
            if (key == addStudent) {
                document.getElementById("2").innerHTML = key + ": " + value;
            }
        });
    };
}

function gradeEdit() {
    var editStudent = document.getElementById("editStu").value;
    var editGrade = document.getElementById("editGrade").value;
    const xhttp = new XMLHttpRequest();
    const url = "https://amhep.pythonanywhere.com/grades/";
    xhttp.open("PUT", url + editStudent, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = { "grade": Number(editGrade) };
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function () {
        data = JSON.parse(this.responseText);
        Object.entries(data).forEach(([key, value]) => {
            if (key == editStudent) {
                document.getElementById("3").innerHTML = key + ": " + value;
            }
        });
    };
}

function removeStudent() {
    var removedStudent = document.getElementById("removeStu").value;
    const xhttp = new XMLHttpRequest();
    const url = "https://amhep.pythonanywhere.com/grades/";
    xhttp.open("DELETE", url + removedStudent, true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send();
    xhttp.onload = function () {
        data = JSON.parse(this.responseText);
        Object.entries(data).forEach(([key, value]) => {
            document.getElementById("4").innerHTML = "Student was removed!"
        });
    };
}