

export default function loginLayout({children}){

    return (
        <nav>
            <ul>
                <li><a>Home</a></li>
                <li>Quieries Generator</li>
                <li>Quit</li>
            </ul>
        </nav>
        {children}
    )

}