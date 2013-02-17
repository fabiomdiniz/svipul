#include "main.hpp"

double prog = 0.0;

double get_prog()
{
	return prog;
}

void work()
{
	using namespace boost;
	python::object views(( 
        python::handle<>( 
            python::borrowed(PyImport_AddModule("svipul.views")))));
	python::object incr_prog = views.attr("incr_prog"); 
	prog = 0.0;
	for(int i = 0; i < 30; ++i)
	{
	    boost::this_thread::sleep(boost::posix_time::seconds(1));
		prog = i/30.0;
		std::cout << prog << std::endl;
		incr_prog();
	}
}

BOOST_PYTHON_MODULE(svipul)
{
    using namespace boost::python;
    def("work", work);
	scope().attr("prog") = prog;
    def("get_prog", get_prog);
}