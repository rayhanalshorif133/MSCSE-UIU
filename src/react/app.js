const App = () => {
  return <div className="mx-auto flex flex-col justify-center items-center">
    <img src="./dist/images/logo.png" alt="uiu logo" className="w-40 p-4 mx-auto text-center mt-10"/>
    <SelectSemester/>
  </div>;
}

const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<App />)