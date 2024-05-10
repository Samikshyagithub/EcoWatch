import Sidebar from '../components/Sidebar'
import FileWindow2 from "../components/fileup2";

const Tool = () => {
  return (
    <>
      <div className="flex w-full h-screen">
        <div className="w-[18%]">
          <Sidebar />
        </div>
        <div className="w-[82%]">
          <FileWindow2></FileWindow2>
        </div>
      </div>
    </>
  )
}

export default Tool
