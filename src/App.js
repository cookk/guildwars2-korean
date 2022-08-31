import React from 'react';
import './App.css';

import '@discretize/gw2-ui-new/dist/default_style.css';
import '@discretize/gw2-ui-new/dist/index.css';
import '@discretize/typeface-menomonia';
import { TraitLine, Skill } from '@discretize/gw2-ui-new'

function App() {
  return (
    <div className="App">
      <TraitLine
        id={40}
        resettable
        selectable
      />
      <TraitLine
        id={41}
        resettable
        selectable
      />
      <TraitLine
        id={42}
        resettable
        selectable
      />
      <TraitLine
        id={43}
        resettable
        selectable
      />
      <Skill id={9093} />
    </div>
  );
}

export default App;
