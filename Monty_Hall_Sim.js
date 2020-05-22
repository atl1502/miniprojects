//The controls for the simulation
let trials = 100000
let switchDoor = true

//Sets a variable to count amount of time correct
let rightAnswers = 0

if (typeof(trials) != "number" || typeof(switchDoor) != "boolean") {
  console.log("Please ensure that you have entered a number for trials and true/false for switchDoor")
} else {
  for (let i = trials; i > 0; --i) {
    //Picks out random doors when called on
    const ranDoorPicker = () => {
      return Math.floor(Math.random() * 3 + 1);
    }

    //Sets the door picks for the door and for the persons pick
    let computerDoor = ranDoorPicker();
    let personDoor = ranDoorPicker();

    //Computer picks a door to randomly eliminate
    const eliminatedDoorPicker = () => {
      let doorTest = ranDoorPicker();
      while (doorTest == computerDoor || doorTest == personDoor) {
        doorTest = ranDoorPicker();
      }
      return doorTest;
    }
    let eliminatedDoor = eliminatedDoorPicker();

    //Switching the persons pick
    let switchedDoor = 6 - personDoor - eliminatedDoor;

    //adds points to overall score
    if (switchDoor == true) {
      if (switchedDoor == computerDoor) {
        ++rightAnswers;
      }
    } else if (switchDoor == false) {
      if (personDoor == computerDoor) {
        ++rightAnswers;
      }
    }
  }
  console.log("Percent correct: " + (rightAnswers * 100) / trials + "%")
}