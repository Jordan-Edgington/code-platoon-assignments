import './App.css'
import { useState } from 'react'
import tasksData from '../tasks.json'


function App() {
  const [tasks, setTasks] = useState(tasksData);
  const [formInput, setFormInput] = useState("");

  const renderTasks = (task) => {
    return `${task.id} | ${task.description}`;
  }

  const createID = (tasksData) => {
    const taskIDs = tasksData.map(task => task.id)
    if (taskIDs.length === 0) {
      return 1
    }
    return Math.max(...taskIDs) + 1
  }

  const newTaskData = { id: (createID(tasks)), description: formInput, completed: false};

  const addTaskHandler = (e) => {
    e.preventDefault();
    if (newTaskData.description === "") {
      alert('You must enter a task!')
    } else if (tasks.map(task => task.description.toLowerCase()).includes(newTaskData.description.toLowerCase())) {
      alert('That task already exists!');
    } else {
    setTasks([...tasks, newTaskData]);
    }
  }
  
  //changes task.completed to the opposite of what it currently is
  const changeComplete = (task) => {
    task.completed ? task.completed=false : task.completed=true;
    setTasks([...tasks]);
  }

  // If the task.completed is True, return completed which will apply the CSS styling of strikethrough
  const strikeThrough = (task) => {
    return task.completed ? "completed" : "notCompleted";
  }

  const createDelete = (task) => {
    return task.completed ? <button id="delete" onClick={(e) => deleteTask(e,task)}>Delete Task</button> : null;
  }

  const deleteTask = (event, task) => {
    event.stopPropagation()
    const taskID = task.id;
    const filteredTasks = tasks.filter((task) => task.id != taskID);
    setTasks(filteredTasks);
  }


  return (
    <>
      <h1>To-Do-List</h1>
      <div className="card">
        <form onSubmit={addTaskHandler} autoComplete="off">
          <input id="textfield" type="text" placeholder="Enter new Task" value={formInput} onChange={(e) => setFormInput(e.target.value)}/>
          <button id="submitButton"> Submit </button>
        </form>
        {/* this ternary will create the to do list if tasks exist, otherwise the unordered list will not occur */}
        {(tasks.length === 0) ? 
          null : 
          <ul id="toDoList">
            {
              tasks.map(task => <li key={task.id} className={strikeThrough(task)} onClick ={() => changeComplete(task)}> {renderTasks(task)} {createDelete(task)}</li>)
            }
          </ul>} 
      </div>
    </>
  )
}

export default App