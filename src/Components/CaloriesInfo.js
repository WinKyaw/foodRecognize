// import React , { Component } from 'react';
// import Forms from 'react-bootstrap/Button';
//
// export default class CaloriesInfo extends React.Component {
//    render(){
//      <div>
//        // <FormControl
//        //   readOnly
//        //   type="text"
//        //   placeholder="Testing"
//        //   // onChange={this.handleChange}
//        // />
//       // test
//      </div>
//    }
// }


import React, { Component } from 'react';
import { Form } from 'react-bootstrap';
export default class CaloriesInfo extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      calories: 0.0
    }
  }
  render() {
    return (
      <div>
        Calories: <Form.Control type="text" placeholder="Readonly input here..." readOnly />
      </div>
    )
  }
}
