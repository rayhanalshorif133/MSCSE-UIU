const Item = () => {
    return <div className="bg-gray-200 h-3 w-3 rounded-full"></div>;
};

const RootTopDesign = () => {
    var j = 5;
    return <div className="absolute top-10 right-10">
        <div className="space-y-4">
            {
                [...Array(5)].map((_, i) => {
                    return <div className="flex space-x-4 justify-end" key={i}>
                       {
                            [...Array(j--)].map((_, i) => {
                                 return <Item key={i} />
                            })
                       }
                    </div>
                })
            }
        </div>
    </div>;
};

const container = document.getElementById('rootTopDesign');
const root = ReactDOM.createRoot(container);
root.render(<RootTopDesign />)