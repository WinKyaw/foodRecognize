import React, { Component } from 'react';
import { Form, Image, Container } from 'react-bootstrap';
export default class FoodInfo extends React.Component {
  constructor(props){
    super(props);
    this.state = {

    }
  }
  render() {
    return (
      <div>
        
        <div>
          <form>
            <label>
              Food:
              <Form.Control type="text" placeholder="Readonly input here..." readOnly />
            </label>

          </form>
        </div>
      </div>
    )
  }
}
