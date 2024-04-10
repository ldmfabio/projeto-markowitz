import React from 'react';
import { Outlet } from 'react-router-dom';
import { Navbar } from '../components/Layout/Navbar';
import { Footer } from '../components/Layout/Footer';

/**



 */
const Layout = ({page_select}) => {
  return (
        <div class="bg-zinc-100 w-screen no-scrollbar">
            <div class="w-11/12 mx-auto">
                <Navbar page_select={page_select} />
                    <main>
                        <Outlet />
                    </main>
                <Footer />
            </div>
        </div>
  );
}

export default Layout