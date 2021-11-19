#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cachy
Version  : 0.3.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/a0/0c/45b249b0efce50a430b8810ec34c5f338d853c31c24b0b297597fd28edda/cachy-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a0/0c/45b249b0efce50a430b8810ec34c5f338d853c31c24b0b297597fd28edda/cachy-0.3.0.tar.gz
Summary  : Cachy provides a simple yet effective caching library.
Group    : Development/Tools
License  : MIT
Requires: cachy-license = %{version}-%{release}
Requires: cachy-python = %{version}-%{release}
Requires: cachy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Cachy
#####
.. image:: https://travis-ci.org/sdispater/cachy.png
:alt: Cachy Build status
:target: https://travis-ci.org/sdispater/cachy

%package license
Summary: license components for the cachy package.
Group: Default

%description license
license components for the cachy package.


%package python
Summary: python components for the cachy package.
Group: Default
Requires: cachy-python3 = %{version}-%{release}

%description python
python components for the cachy package.


%package python3
Summary: python3 components for the cachy package.
Group: Default
Requires: python3-core
Provides: pypi(cachy)

%description python3
python3 components for the cachy package.


%prep
%setup -q -n cachy-0.3.0
cd %{_builddir}/cachy-0.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637363159
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cachy
cp %{_builddir}/cachy-0.3.0/LICENSE %{buildroot}/usr/share/package-licenses/cachy/98a929dd0a579b9761599bc34c800296ad986dcd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cachy/98a929dd0a579b9761599bc34c800296ad986dcd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
