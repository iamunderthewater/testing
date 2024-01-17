
const person1 = { firstName: 'Alan', 
                    age: 27,
                    hobbies: ['jogging', 'swimming', 'golf']  }

const person2 = { firstName: 'Bill', 
                    age: 33,
                    hobbies: ['golf', 'reading']  }

const person3 = { firstName: 'Clair', 
                    age: 22,
                    hobbies: ['singing', 'dancing', 'golf']  }

// const member = [ person1, person2, person3]

const member = [];


// function initArray() {

//    if ( runFlag == true ) {
//    member.push(person1);
//    member.push(person2);
//    member.push(person3);
//    }
// }

function showMember () { 

            console.log('at show member >', member);
            document.getElementById('demo').innerHTML='';

            member.forEach( e => { 
                
                console.log('person > ', e);
                let hobbyStr = e.hobbies.join(', '); 
                let memberInfo = `<li>First name: ${ e.firstName } <br> Age: ${e.age} <br> Hobby: ${ hobbyStr } <br> Email:${e.email} </li>`
             // document.querySelector('#demo').innerHTML += e.firstName + e.age + e.hobby + '<br>';

             document.querySelector('#demo').innerHTML += memberInfo + '<br>';

            } );

           


}

function addMember() {

   let getName = document.getElementById('name').value;
   let getAge = document.getElementById('age').value;
   let getHobbies = document.getElementById('hobby').value.split(',');
   let getEmail = document.getElementById("email;").value;

   let myMember = { firstName: getName,
                    age: getAge,
                    hobbies: getHobbies,
                    email: getEmail
                    };  

    console.log('member object :', myMember);
    member.push(myMember);

    document.getElementById('show').click();

    document.getElementById('myform').reset();
    
}

// document.querySelector('#demo').innerHTML = show;