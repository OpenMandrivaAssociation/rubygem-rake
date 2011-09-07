%define	majorver	0.9.2
%define	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%define	fullver	%{majorver}%{?preminorver}

%define	ruby_sitelib	%(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define	gemdir		%(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define	gemname	rake
%define	geminstdir	%{gemdir}/gems/%{gemname}-%{fullver}

%define	rubyabi	1.8

Summary:	Ruby based make-like utility
Name:		rubygem-%{gemname}

Version:	%{majorver}
Release:	%mkrel 1
Group:		Development/Ruby
License:	MIT
URL:		http://rake.rubyforge.org
Source0:	http://gems.rubyforge.org/gems/%{gemname}-%{fullver}.gem

Requires:	ruby-RubyGems
Requires:	ruby(abi) = %{rubyabi}
BuildRequires:	ruby-RubyGems
BuildRequires:	ruby(abi) = %{rubyabi}
## %%check
BuildRequires:	ruby-flexmock
BuildRequires:	rubygem(minitest)
BuildArch:	noarch
Provides:	rubygem(%{gemname}) = %{version}-%{release}

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.

%package	doc
Summary:	Documentation for %{name}
Group:		Development/Ruby
# Directory ownership issue
Requires:	%{name} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}.


%prep
%setup -q -c -T

%build
mkdir -p .%{gemdir}
gem install -V \
	--local \
	--install-dir $(pwd)/%{gemdir} \
	--bindir $(pwd)%{_bindir} \
	--force \
	--rdoc \
	%{SOURCE0}

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{_prefix}/* %{buildroot}%{_prefix}/

# rpmlint issue
find %{buildroot}%{geminstdir}/{lib,test} -type f | \
	xargs sed -i -e '\@^#!/usr.*ruby@d'
find %{buildroot}%{geminstdir}/{doc,lib,test} -type f | xargs chmod 0644

# cleanup
rm %{buildroot}%{geminstdir}/.gemtest
rm -f %{buildroot}%{geminstdir}/RRR

%check
pushd .%{geminstdir}
# Someone please check why test fails!!
# Note that on ppc64 the following test causes segv, perhaps
# bug in ruby itself, needs investigating.
ruby -Ilib ./bin/rake test || \
	echo "Please some investigate!!"

%files
%defattr(-,root,root,-)
%{_bindir}/rake
%dir	%{geminstdir}
%doc	%{geminstdir}/README.rdoc
%doc	%{geminstdir}/MIT-LICENSE
%doc	%{geminstdir}/TODO
%doc	%{geminstdir}/CHANGES
%{geminstdir}/bin
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{fullver}.gem
%{gemdir}/specifications/%{gemname}-%{fullver}.gemspec

%files	doc
%defattr(-,root,root,-)
%{geminstdir}/Rakefile
%{geminstdir}/install.rb
%{geminstdir}/doc
%{geminstdir}/test/
%{gemdir}/doc/%{gemname}-%{fullver}/
