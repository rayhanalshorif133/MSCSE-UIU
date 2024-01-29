const App = () => {
  return <div className="mx-auto flex justify-center items-center">
    <SelectSemester />
  </div>;
}

const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<App />)