import React from 'react'

import ExcerciseItem from "./Exercise";

function ExerciseView(props) {
    return (
        <div>
            <ul>
                {props.exerciseList.map(exercise => <ExcerciseItem exercise={exercise} /> )}
            </ul>
        </div>
    )
}

export default ExerciseView