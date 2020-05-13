Name:       python3-sortedcontainers
Summary:    Sorted collections library
Version:    2.10
Release:    1
License:    ASL 2.0
URL:        https://pypi.org/project/sortedcontainers/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Sorted collections library, written in pure-Python, and fast as C-extensions.

%prep
%setup -q -n %{name}-%{version}/sortedcontainers

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%{python3_sitearch}/sortedcontainers
%{python3_sitearch}/sortedcontainers-*.egg-info
