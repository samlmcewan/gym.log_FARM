import axios from 'axios'
import React from 'react'

function ExerciseItem(props) {
    const deleteExerciseHandler = (title) => {
        axios.delete('http://localhost:8000/api/exercise/${title}').then(res => 
            console.log(res.data))}
            return (
                <div>
                    <h3>{props.exercise.title}</h3>
                    <p>{props.exercise.description}</p>
                    <button onClick={() => deleteExerciseHandler(props.exercise.title)} className="btn btn-primary m-2">x</button>
                </div>
            )
    }

    export default ExerciseItem;