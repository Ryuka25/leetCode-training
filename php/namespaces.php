<?php 

namespace Framework
{
    class Hello 
    {
        public function World()
        {
            echo "Hello World";
        }
    }
}

namespace Foo
{
    
    // Allows us to refer to the class Hello
    // without specifying its namespace each time
    use Framework\Hello as Hello;

    class Bar 
    {
        function bar()
        {
            // here we can refer to Framework\Hello as simply Hello
            // due to the preceding "use" statement
            $hello = new Hello();
            $hello->World();
        }
    }
}

namespace
{
    $hello = new Framework\Hello();
    $hello->World();            // 'Hello World'

    $foo = new Foo\Bar();
    $foo->bar();                // 'Hello World'
}