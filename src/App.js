import React from 'react';
import './App.css';

import 'discretize-monorepo-root/gw2-ui/dist/default_style.css';
import 'discretize-monorepo-root/gw2-ui/dist/index.css'
import 'discretize-monorepo-root/typeface-menomonia';

import { Trait, TraitLine, Skill } from 'discretize-monorepo-root/gw2-ui'

function App() {
  return (
    <div className="App">
      <TraitLine
        id={41}
        resettable
        selectable
      />
      <Trait
        id={227}
      />
      <Skill
        id={62797}
      />
    </div>
  );
}

export default App;
