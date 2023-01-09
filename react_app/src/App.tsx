import './App.css';
import React, { useEffect, useState } from 'react';
import { EuiProvider, EuiBasicTable, EuiFlexGroup, EuiSpacer, EuiPage, EuiPageHeader, EuiButtonIcon, EuiListGroup, EuiListGroupItem, EuiText} 
from '@elastic/eui';
import "@elastic/eui/dist/eui_theme_dark.css";
import "@elastic/eui/dist/eui_theme_light.css";

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
  const [itemIdToExpandedRowMap, setItemIdToExpandedRowMap] = useState({});
  const [routeStopData, setRouteStopData] = useState<string[]>([])

  const { routes } = props

  const toggleStopDetails = item => {
    const itemIdToExpandedRowMapValues = { ...itemIdToExpandedRowMap };
    if (itemIdToExpandedRowMapValues[item.id]) {
      delete itemIdToExpandedRowMapValues[item.id];
      setItemIdToExpandedRowMap(itemIdToExpandedRowMapValues);
      return;
    }

    fetch(`http://localhost:5000/get_mbta_subway_stops/${item.id}`)
      .then(response => response.json())
      .then(data => {
        // This is a massive hack. I should be creating a state object of pattern {<route-type>: <stop_list>}
        // and then updating that once we receive the value of the results.
        const stopsElms = data["stops"].map(s => {
          return <EuiListGroupItem label={s} />
        })
        itemIdToExpandedRowMapValues[item.id] = (
          <EuiListGroup size="s" gutterSize="none"><EuiText><h5>Stops:</h5></EuiText>{stopsElms}</EuiListGroup>
        )
        setItemIdToExpandedRowMap(itemIdToExpandedRowMapValues);
      })
  };

  const columns = [
    {
      field: 'id',
      name: 'Route ID',
      width: '40%',
    },
    {
      field: 'name',
      name: 'Route Name',
      width: '40%'
    },
    {
      name: 'View Stops',
      width: '20%',
      isExpander: true,
      render: (item) => (
        <EuiButtonIcon
          onClick={() => toggleStopDetails(item)}
          aria-label={itemIdToExpandedRowMap[item.id] ? 'Collapse' : 'Expand'}
          iconType={
            itemIdToExpandedRowMap[item.id] ? 'arrowDown' : 'arrowRight'
          }
        />
      ),
    },
  ];

  const sorting = {
    sort: {
      field: 'id',
      direction: 'asc' as const,
    },
    enableAllColumns: false,
    readOnly: false,
  };

  return (
    <EuiBasicTable
      tableCaption="Basic Subway Routes"
      items={routes}
      columns={columns}
      itemId="id"
      isExpandable={true}
      itemIdToExpandedRowMap={itemIdToExpandedRowMap}
      sorting={sorting}
    />
  );
};

function App() {
  const [routeData, setRouteData] = useState<Route[]>([]);

  useEffect(()=>{
    fetch('http://localhost:5000/get_mbta_subway_routes')
    .then(response => response.json())
    .then(data => setRouteData(data["routes"]))
    .catch(error => console.log(error))
  }, []);

  return (
    <EuiProvider colorMode='light'>
      <EuiPageHeader
        pageTitle="MBTA Demo"
        iconType="logoKibana"
        description="Below are the currently available MBTA subway routes"
        paddingSize="l"
      />
      <EuiSpacer size="l" />
      <EuiPage paddingSize="l">
        <EuiFlexGroup className="eui-fullHeight">
          <Table routes={routeData}></Table>
        </EuiFlexGroup>
      </EuiPage>
    </EuiProvider>
  );

}



export default App;