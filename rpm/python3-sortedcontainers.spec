# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-sortedcontainers
Summary:    Sorted collections library
Version:    2.10
Release:    1
License:    ASL 2.0
URL:        https://pypi.org/project/sortedcontainers/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-setuptools

%description
Sorted collections library, written in pure-Python, and fast as C-extensions.

%prep
%setup -q -n %{name}-%{version}/sortedcontainers

%build
python3 ./setup.py build

%install
rm -rf %{buildroot}
python3 ./setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/sortedcontainers
%{python3_sitearch}/sortedcontainers-*.egg-info
