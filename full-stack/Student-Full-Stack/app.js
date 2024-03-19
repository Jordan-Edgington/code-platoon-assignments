const createStudentLI = (student) => {
    const studentsList = document.getElementById("students");
    let newLI = document.createElement("li");
    newLI.class = "student"
    newLI.innerHTML = `ID: ${student.id} | Name: ${student.first_name} ${student.last_name} | Age: ${student.age} | Grade: ${student.grade}`;
    studentsList.appendChild(newLI);
}

const resetList = () => {
    const studentsList = document.getElementById("students");
    studentsList.innerHTML = "";
}

const getStudents = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/v1/students");
    let students = await response.json();
    resetList();
    students.map((stud) => {
        let {id, first_name, last_name, age, grade} = stud;
        createStudentLI(stud);
    })
}

const getOldStudents = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/v1/old_students");
    let students = await response.json();
    resetList();
    students.map((stud) => {
        let {id, first_name, last_name, age, grade} = stud;
        createStudentLI(stud);
    })
}

const getYoungStudents = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/v1/young_students");
    let students = await response.json();
    resetList();
    students.map((stud) => {
        let {id, first_name, last_name, age, grade} = stud;
        createStudentLI(stud);
    })
}

const getAdvanceStudents = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/v1/advance_students");
    let students = await response.json();
    resetList();
    students.map((stud) => {
        let {id, first_name, last_name, age, grade} = stud;
        createStudentLI(stud);
    })
}

const getStudentNames = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/v1/student_names/");
    let students = await response.json();
    resetList();
    students.map((stud) => {
        let {first_name, last_name} = stud;
        //Have to manually create the list elements because these don't have all the objects that the above filters did.
        const studentsList = document.getElementById("students");
        let newLI = document.createElement("li");
        newLI.class = "student"
        newLI.innerHTML = `Name: ${stud.first_name} ${stud.last_name}`;
        studentsList.appendChild(newLI);
        })
}


const getStudentAges = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/v1/student_ages/");
    let students = await response.json();
    resetList();
    students.map((stud) => {
        let {age, full_name} = stud;
        //Have to manually create the list elements because these don't have all the objects that the above filters did.
        const studentsList = document.getElementById("students");
        let newLI = document.createElement("li");
        newLI.class = "student"
        newLI.innerHTML = `Age: ${stud.age} | Name: ${stud.full_name}`;
        studentsList.appendChild(newLI);
        })
}