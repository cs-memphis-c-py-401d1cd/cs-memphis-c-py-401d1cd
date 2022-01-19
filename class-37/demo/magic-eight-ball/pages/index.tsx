import Head from 'next/head'

export default function Home() {

  {/* Handle Form Submission */ }
  function questionAskedHandler(evt: any) {
    evt.preventDefault();
    alert(evt.target.question.value);
  }

  return (
    <div className="">
      <Head>
        <title>Expert 8 Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-50">
        <h1 className="text-4xl text-gray-50">Expert 8 Ball</h1>
      </header>

      {/* Question Form */}
      <form onSubmit={questionAskedHandler} className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200">
        <input name="question" className="flex-auto pl-1" />
        <button className="px-2 py-1 bg-gray-500 text-gray-50">Ask</button>
      </form>

      {/* Eight Ball */}
      <div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
        <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
          <p className="text-xl text-center">Ask me anything</p>
        </div>
      </div>

      <footer className="p-4 mt-8 bg-gray-500 text-gray-50">
        2022 Code School
      </footer>
    </div>
  )
}