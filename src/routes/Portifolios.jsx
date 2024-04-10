import React, { useState } from 'react'
import '../App.css'

const Wallets = () => {
  const [wallets, setWallets] = useState([
    {
      id: 1,
      name: 'Carteira 1',
      stocks: [
        'Stock 1',
        'Stock 2',
        'Stock 3',
        'Stock 4',
        'Stock 5'
      ]
    },
    {
      id: 2,
      name: 'Carteira 2',
      stocks: [
        'Stock 1',
        'Stock 2',
        'Stock 3',
        'Stock 4',
        'Stock 5'
      ]
    },
    {
      id: 3,
      name: 'Carteira 3',
      stocks: [
        'Stock 1',
        'Stock 2',
        'Stock 3',
        'Stock 4',
        'Stock 5'
      ]
    },
    {
      id: 4,
      name: 'Carteira 4',
      stocks: [
        'Stock 1',
        'Stock 2',
        'Stock 3',
        'Stock 4',
        'Stock 5'
      ]
    },
    {
      id: 5,
      name: 'Carteira 5',
      stocks: [
        'Stock 1',
        'Stock 2',
        'Stock 3',
        'Stock 4',
        'Stock 5'
      ]
    },
    {
      id: 6,
      name: 'Carteira 6',
      stocks: [
        'Stock 1',
        'Stock 2',
        'Stock 3',
        'Stock 4',
        'Stock 5'
      ]
    },
    {
      id: 7,
      name: 'Carteira 7',
      stocks: [
        'Stock 1',
        'Stock 2',
        'Stock 3',
        'Stock 4',
        'Stock 5'
      ]
    },
    {
      id: 8,
      name: 'Carteira 8',
      stocks: [
        'Stock 1',
        'Stock 2',
        'Stock 3',
        'Stock 4',
        'Stock 5'
      ]
    }
  ])

  const addNewWallet = () => {
    const newWallet = {
      id: wallets.length + 1,
      name: `Carteira ${wallets.length + 1}`,
      stocks: [
        'Stock 1',
        'Stock 2',
        'Stock 3',
        'Stock 4',
        'Stock 5'
      ]
    }

    setWallets([...wallets, newWallet])
  }

  return (
    <>
      <section className='flex flex-wrap justify-center gap-10 mt-8'>
        <div onClick={() => addNewWallet()} className='w-1/6 p-8 flex justify-center items-center bg-blue-600 shadow-local rounded-3xl hover:bg-blue-500 cursor-pointer'>
          <h2 className='text-3xl text-white'>+</h2>
        </div>
        {wallets.map((wallet) => (
          <div key={wallet.id} className='w-1/6 p-8 bg-white shadow-local rounded-3xl'>
            <h2 className='text-xl'>{wallet.name}</h2>
            <ul className='mt-3 pl-5'>
              {wallet.stocks.map((stock, index) => (
                <li key={index} className='text-gray-500 list-disc'>{stock}</li>
              ))}
            </ul>
          </div>
        ))}
      </section>
    </>
  )
}

export default Wallets