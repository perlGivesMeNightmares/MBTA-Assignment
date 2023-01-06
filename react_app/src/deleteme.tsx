import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState, ReactElement } from 'react';
import { formatDate, EuiInMemoryTable, EuiLink, EuiHealth, EuiProvider, EuiText, EuiBasicTable, EuiPageTemplate, EuiFlexGroup, EuiFlexItem, EuiSpacer, EuiPage,
  EuiPageTemplateProps, EuiPageHeaderProps, } 
from '@elastic/eui';
import "@elastic/eui/dist/eui_theme_dark.css";
import { useEuiTheme } from '@elastic/eui';
import { css } from '@emotion/react';

/*
Example route object:

{
  id: 'red',
  name: 'Red Line'
}

*/


type Route = {
  id: string,
  name: string
}

type TableProps = {
  routes: Route[]
}

export const Table: React.FC<TableProps> = ( props: TableProps ) => {
  const { routes } = props
  console.log("props are " + JSON.stringify(props));
  const columns = [
    {
      field: 'id',
      name: 'Route ID',
      sortable: true,
      width: '40%'
    },
    {
      field: 'name',
      name: 'Route Name',
      width: '40%'
    },
    // {
    //   field: 'online',
    //   name: 'Online',
    //   dataType: 'boolean',
    //   render: (online) => {
    //     const color = online ? 'success' : 'danger';
    //     const label = online ? 'Online' : 'Offline';
    //     return <EuiHealth color={color}>{label}</EuiHealth>;
    //   },
    //   sortable: true,
    // },
  ];

  // const sorting = {
  //   sort: {
  //     field: 'id',
  //     direction: 'desc',
  //   },
  // };

  return (
    <EuiInMemoryTable
      tableCaption="Basic Subway Routes"
      items={routes}
      columns={columns}
      tableLayout={"auto"}
    />
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
    <EuiProvider colorMode='light'>
      <EuiPage paddingSize="none" grow={true}>
        <Table routes={routeData}></Table>
      </EuiPage>
    </EuiProvider>
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