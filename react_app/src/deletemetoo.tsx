import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState, ReactElement } from 'react';
import Dropdown from 'react-bootstrap/Dropdown';

/*
Example route object:

{
  id: 'red',
  name: 'Red Line'
}

*/

const newRouteSelected = (routes) => {
  console.log("routes are " + JSON.stringify(routes))
  return;
}


type Route = {
  id: string,
  name: string
}

type SelectProps = {
  routes: Route[]
}

export const RouteOption = ( { routeOption } ) => {
  console.log("route option is " + JSON.stringify(routeOption));
  return (
    <Dropdown.Item>Hurr</Dropdown.Item>
  )
}

export const RouteSelection: React.FC<SelectProps> = ( props: SelectProps ) => {
  const { routes } = props
  console.log("props are " + JSON.stringify(props));
  const options = routes.map(r => {
    return {'key': r.id, 'label': `${r.id} - ${r.name}`};
  });
  console.log('options are ' + JSON.stringify(options))
  return (
    <Dropdown>
      <Dropdown.Toggle variant="success" id="dropdown-basic">
        View Routes
      </Dropdown.Toggle>

      <Dropdown.Menu>
        <RouteOption routeOption={routes[0]}></RouteOption>
        <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
        <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
      </Dropdown.Menu>
    </Dropdown>
  );
};

function App() {
  const [routeData, setRouteData] = useState<Route[]>([]);

  useEffect(()=>{
    fetch('http://localhost:5000/get_mbta_subway_routes')
    .then(response => response.json())
    .then(data => setRouteData(data))
    .catch(error => console.log(error))
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <RouteSelection routes={routeData}></RouteSelection>
      </header>
    </div>
);

  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <Table routes={routeData}></Table>
  //       <div>{routeData ? 
  //         <h3>{JSON.stringify(routeData)}</h3>
  //         :
  //         <h3>LOADING</h3>}</div>
  //     </header>
  //   </div>
  // );
}



export default App;