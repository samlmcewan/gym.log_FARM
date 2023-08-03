import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'

function App() {

  const [exerciseList, setExerciseList] = useState([{}])
  const [title, setTitle] = useState('')
  const [desc, setDesc] = useState('')

  // Read all excercises 
  useEffect(() => {
    axios.get('http://localhost:8000/api/exercise')
    .then(res => {
        setExerciseList(res.data)
    })
  });

  // Post an exercise 
  const addExerciseHandler = () => {
    axios.post('http://localhost:8000/api/exercise', {'title':title, 'description': desc})
    .then(res => console.log(res))
  };


  return (
    <div className="App">
      Hello world
      <div className="list-group-item justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}}>
        <h1>gym.log()</h1>
        <div className="card">
          <div className="card-body">
            <h2>Add Excercise</h2>
            <div className="card-text">
              <input className="mb-2 form-control titleIn" placeholder="Title" onChange="{event => setTitle(event.target.value)}"/>
              <input className="mb-2 form-control descIn" placeholder="Description" onChange="{event => setDesc(event.target.value)}"/>
              <button className="btn btn-outline-primary mx-2" style={{"borderRadius":"50px", "font-weight":"bold"}} onClick={addExerciseHandler}>Add exercise</button>
            </div>
          </div>
        </div>

        <div className="card">
          <h2>All exercises</h2>
          <div>
            {/* Exercises - external component */}
          </div>
        </div>
     
      </div>
    </div>
  );
}

export default App;
